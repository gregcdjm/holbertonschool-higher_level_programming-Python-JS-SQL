#!/usr/bin/node

const gangster = process.argv;
const gang = parseInt(gangster[2]);
let x;

if (isNaN(gang)) {
  console.log('Missing size');
} else
  for (x = 0; x < gang; x++) {
    console.log('X'.repeat(gang));
  }
}
