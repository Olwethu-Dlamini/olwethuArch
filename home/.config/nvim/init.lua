-- Minimal Neovim config, no plugins. Everything here is built into Neovim.
local o = vim.opt

o.number = true
o.relativenumber = true
o.cursorline = true
o.termguicolors = true
o.signcolumn = "yes"
o.scrolloff = 8
o.wrap = false

-- indentation
o.expandtab = true
o.shiftwidth = 4
o.tabstop = 4
o.smartindent = true

-- search
o.ignorecase = true
o.smartcase = true
o.hlsearch = true

-- sharing the clipboard with Wayland (needs wl-clipboard)
o.clipboard = "unnamedplus"

-- splits open right/below
o.splitright = true
o.splitbelow = true

-- keep undo history between sessions
o.undofile = true

-- faster UI feedback
o.updatetime = 250

vim.g.mapleader = " "

local map = vim.keymap.set
map("n", "<leader>w", "<cmd>w<cr>", { desc = "Save" })
map("n", "<leader>q", "<cmd>q<cr>", { desc = "Quit" })
map("n", "<Esc>", "<cmd>nohlsearch<cr>", { desc = "Clear search highlight" })
map("n", "<leader>e", "<cmd>Explore<cr>", { desc = "File explorer (netrw)" })

-- window navigation
map("n", "<C-h>", "<C-w>h")
map("n", "<C-j>", "<C-w>j")
map("n", "<C-k>", "<C-w>k")
map("n", "<C-l>", "<C-w>l")

-- move selected lines up/down
map("v", "J", ":m '>+1<cr>gv=gv")
map("v", "K", ":m '<-2<cr>gv=gv")

-- briefly highlight yanked text
vim.api.nvim_create_autocmd("TextYankPost", {
  callback = function() vim.highlight.on_yank() end,
})
