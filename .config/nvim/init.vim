set autoindent
set backupdir=~/.cache/vim
set clipboard=unnamedplus
set cursorline
set expandtab
set hlsearch
set ignorecase
set incsearch
set laststatus=2
set modeline
set mouse=v
set noshowmode
set noswapfile
set number
set relativenumber
set shiftwidth=4
set showmatch
set showtabline=2
set softtabstop=4
set tabstop=4
set wildmenu
set wildmode=longest,list

:command EX Explore
:command PI PlugInstall
:command PC PlugClean
:command NT NERDTree

filetype plugin on
filetype plugin indent on

" vim-plug
call plug#begin('~/.config/nvim/plugged')
    Plug 'catppuccin/nvim', {'as': 'catppuccin'}
    Plug 'scrooloose/nerdtree', { 'on':  'NERDTreeToggle' }
    Plug 'preservim/nerdcommenter'
    Plug 'neoclide/coc.nvim', {'branch': 'release'}
    Plug 'codechips/coc-svelte', {'do': 'npm install'}
    Plug 'justinmk/vim-sneak'
    Plug 'nvim-lualine/lualine.nvim'
    Plug 'kyazdani42/nvim-web-devicons'
    Plug 'sheerun/vim-polyglot'
call plug#end()

" colorscheme
if (has('termguicolors'))
    set termguicolors
endif

syntax enable
colorscheme catppuccin

" vim-sneak
let g:sneak#label = 1
nmap f <Plug>Sneak_s
nmap F <Plug>Sneak_S

" NERDTree
nmap <C-n> :NERDTreeToggle<CR>

" lualine
lua << END
require('lualine').setup()
END
