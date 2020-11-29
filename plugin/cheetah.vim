" $Id$
" Name Of File: |n|
"
"  Description: Vim plugin
"
"       Author: Ivan Carlos S. Lopes <lopesivan (at) poli (dot) com (dot) br>
"   Maintainer: Ivan Carlos S. Lopes <lopesivan (at) poli (dot) com (dot) br>
"
"  Last Change: $Date:$
"      Version: $Revision:$
"
"    Copyright: This script is released under the Vim License.
"

if &cp || exists("g:loaded_cheetah")
    finish
endif

let g:loaded_cheetah = "v01"
let s:keepcpo  = &cpo
set cpo&vim

" ----------------------------------------------------------------------------
if !has('python') && !has('python3')
    echo "Error: Required vim compiled with +python"
    finish
endif

function Cheetah()
	let plugin_name = "cheetah"
	let path = expand('$HOME').'/.config/nvim/local-plugins/'.plugin_name.'/plugin/'
	let main = path . "main.py"
    exec "pyfile ".main
endfunction

call Cheetah()

command Cheetah :py cheetahMainTemplate()
command CheetahInput :py cheetahPythonInput()
" ----------------------------------------------------------------------------

let &cpo=s:keepcpo
unlet s:keepcpo

" vim: ts=4
