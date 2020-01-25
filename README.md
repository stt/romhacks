# Community repository for exchanging arcade romhacks

## Have an arcade game ...
... you've fixed up the cabinet and it's really awesome except for that one little thing that the game itself does? Attract mode makes annoying noises? Hiscore list is barely shown at all?

Whatever it is, create an issue on this repository and spread the message. Might take a while but there's likely someone out there to help you. (If you feel it needs attention sooner rather than later, there's the option of getting [Bountysource](https://www.bountysource.com/) involved.)

## Have experience with assembly and emulators ...
... and you're looking for something to do?

Take a look at the issues list and feel free to contribute!

## Usage of mame patches

`git clone` this repo (or download zip under the green button) into your mame directory and open one of the hacks in shell (e.g. `cd galaxian`) do './ha init' to extract rom binaries from mame's roms directory, `./ha ap` to assemble and patch and `./ha play` to start patched roms in mame.

## Requirements

Requires: [mame](https://github.com/mamedev/mame/releases), python3 and depending on use: [z80asm](https://github.com/z88dk/z88dk/releases), [asm6](https://wiki.nesdev.com/w/index.php/Tools), [vasmm68k](https://www.chibiakumas.com/68000/68000DevTools.php)

On macos z80asm and asm6 are in homebrew core, for vasmm68k you could try:

    brew tap Kalmalyzer/vasmm68k-macosx https://github.com/Kalmalyzer/vasmm68k-macosx
    brew install kalmalyzer/vasmm68k-macosx/vasmm68k
