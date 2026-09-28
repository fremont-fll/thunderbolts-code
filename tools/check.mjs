#!/usr/bin/env node
// Checks the programs in this repo. Runs in GitHub Actions on every push and pull request.
//
// For every Pybricks block program (programs/<name>.py) it verifies that
//   1. the "# pybricks blocks file:" header holds valid Pybricks JSON, and
//   2. programs/<name>.words.py, the readable Python copy, matches the Python in the program.
// Plain Python programs are skipped. No dependencies.
import { existsSync, readdirSync, readFileSync } from "node:fs";
import { pathToFileURL } from "node:url";

const PREFIX = "# pybricks blocks file:";
const isProgram = (path) => /^programs\/[^/]+\.py$/.test(path) && !/\.(words|theirs|mine)\.py$/.test(path);

/** @param {Record<string, string>} files path -> text. Returns a list of problems (empty if all is well). */
export function checkPrograms(files) {
    const problems = [];
    for (const [path, text] of Object.entries(files)) {
        if (!isProgram(path) || !text.startsWith(PREFIX)) continue;

        const newline = text.indexOf("\n");
        try {
            const json = text.slice(PREFIX.length, newline === -1 ? text.length : newline).replace(/\r$/, "");
            if (JSON.parse(json)?.info?.type !== "pybricks") throw new Error("not a Pybricks workspace");
        } catch (e) {
            problems.push(`${path}: the blocks header is damaged (${e.message}). Re-export it from Pybricks Code.`);
            continue;
        }

        const words = newline === -1 ? "" : text.slice(newline + 1);
        const wordsFile = path.replace(/\.py$/, ".words.py");
        if (files[wordsFile] === undefined) {
            problems.push(`${path}: ${wordsFile} is missing. Push it again from Pybricks Sync.`);
        } else if (files[wordsFile] !== words) {
            problems.push(`${path}: ${wordsFile} is out of date. Push it again from Pybricks Sync.`);
        }
    }
    return problems;
}

function readPrograms(dir = "programs") {
    const files = {};
    if (!existsSync(dir)) return files;
    for (const name of readdirSync(dir)) {
        if (name.endsWith(".py")) files[`${dir}/${name}`] = readFileSync(`${dir}/${name}`, "utf8");
    }
    return files;
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
    const files = readPrograms();
    const problems = checkPrograms(files);
    for (const p of problems) console.error(`✗ ${p}`);
    const count = Object.keys(files).filter(isProgram).length;
    console.log(problems.length === 0 ? `✓ ${count} programs checked` : `${problems.length} problem(s) in ${count} programs`);
    process.exit(problems.length === 0 ? 0 : 1);
}
