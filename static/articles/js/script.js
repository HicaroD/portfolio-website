let base_colorscheme_url = "//unpkg.com/@highlightjs/cdn-assets@11.5.1/styles/";
let colorschemes = new Map([
    ["atom", "atom-one-dark.min.css"],
    ["github", "github-dark.min.css"],
    ["monokai", "monokai.min.css"],
    ["stack-overflow", "stackoverflow-dark.min.css"],
    ["nord", "nord.min.css"],
    ["gruvbox", "base16/gruvbox-dark-hard.min.css"],
])
let colorscheme_link = document.getElementById("colorscheme");

for (const [colorscheme, colorscheme_path] of colorschemes) {
    document.getElementById(colorscheme).onclick = function() {
        colorscheme_link.href = base_colorscheme_url + colorscheme_path;
    };
}

hljs.highlightAll();
