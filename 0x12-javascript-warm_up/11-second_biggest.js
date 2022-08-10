#!/usr/bin/node

const entry = process.argv;
let check;
let big = 0;
let secondbig = 0;

for (let i = 2; i < entry.length; i++) {
    check = parseInt(entry[i]);
    if (isNaN(check)) {
	continue;
    }
    if (check >= big) {
	    secondbig = big;
	    big = check;
    }
}
console.log(secondbig);
