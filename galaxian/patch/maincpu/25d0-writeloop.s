
        ld   a,$10               ; empty character
        ld   b,$1A               ; # of chars to clear
        ld   de,$0020            ; # of chars until next col (32)
loop:
        ld   (hl),a              ; write char
        add  hl,de               ; next col
        djnz loop                ; loop to PC-2
        ret                      ; done

