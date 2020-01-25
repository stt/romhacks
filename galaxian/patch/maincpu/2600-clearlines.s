
        call $0598               ; do colour attribs we overwrote at $0215
        ld   a,($4002)           ; read credits
        and  a                   ; set zero flag
        ret  nz                  ; return if credits>0
        ld   hl,$5060            ; clear "1UP" line
        call $25D0
        ld   hl,$5061            ; clear score line
        call $25D0
        ld   hl,$505E            ; clear line above credits (top of flags after game)
        call $25D0
        ld   hl,$505F            ; clear credits line
        call $25D0
        ret
