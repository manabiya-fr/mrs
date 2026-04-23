window.MathJax = {
	tex: {
		inlineMath: [["\\(", "\\)"]],
		displayMath: [["\\[", "\\]"]],
		processEscapes: true,
		processEnvironments: true,
		macros: {
			minimize: ["\\mathop{\\mbox{minimize}}_{#1}\\,", 1]
		},
	},
	options: {
		ignoreHtmlClass: ".*|",
		processHtmlClass: "arithmatex"
	}
};

document$.subscribe(() => {
	MathJax.startup.output.clearCache()
	MathJax.typesetClear()
	MathJax.texReset()
	MathJax.typesetPromise()
})
