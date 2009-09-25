 /* OCaml brush contributed by David Simmons-Duffin */
SyntaxHighlighter.brushes.OCaml = function()
{
    var standardmodules =
	'Arg Array ArrayLabels Buffer Callback Char Complex Digest ' +
	'Filename Format Gc Genlex Hashtbl Int32 Int64 Lazy Lexing ' +
	'List ListLabels Map Marshal MoreLabels Nativeint Oo Parsing ' +
	'Printexc Printf Queue Random Scanf Set Sort Stack StdLabels ' +
	'Stream String StringLabels Sys Weak';
    var funcs = 
	'raise invalid_arg failwith compare min max not succ pred abs ' +
	'max_int min_int lnot sqrt exp log cos sin tan acos asin atan cosh ' +
	'sinh tanh ceil floor abs_float mod_float frexp ldexp modf float ' +
	'float_of_int truncate int_of_float infinity neg_infinity nan max_float ' +
	'min_float epsilon_float classify_float int_of_char char_of_int ignore ' +
	'string_of_bool bool_of_string string_of_int int_of_string string_of_float ' +
	'float_of_string fst snd stdin stdout stderr print_char print_string ' +
	'print_int print_float print_endline print_newline prerr_char prerr_string ' +
	'prerr_int prerr_float prerr_endline prerr_newline read_line read_int ' +
	'read_float open_out open_out_bin open_out_gen flush flush_all output_char ' +
	'output_string output output_byte output_binary_int output_value seek_out  ' +
	'pos_out out_channel_length close_out close_out_noerr set_binary_mode_out ' +
	'open_in open_in_bin open_in_gen input_char input_line input really_input ' +
	'input_byte input_binary_int input_value seek_in pos_in in_channel_length ' +
	'close_in close_in_noerr set_binary_mode_in seek_out pos_out out_channel_length ' +
	'seek_in pos_in in_channel_length ref incr decr string_of_format format_of_string ' +
	'exit at_exit valid_float_lexem unsafe_really_input do_at_exit ' +
	standardmodules.split(' ').join('.\\w+ ');

    var keywords =  
	'and as assert asr begin class constraint do done downto else end ' +
	'exception external false for fun function functor if in include ' +
	'inherit initializer land lazy let lor lsl lsr lxor match method ' +
	'mod module mutable new object of open or private rec sig struct ' +
	'then to true try type val virtual when while with';

    
    this.regexList = [
        { regex: /\(\*[\s\S]*?\*\)/gm,                          css: 'comments'     }, // multiline comments (* *)
	{ regex: SyntaxHighlighter.regexLib.doubleQuotedString, css: 'string'       },
	{ regex: SyntaxHighlighter.regexLib.singleQuotedString, css: 'string'       },
	{ regex: new RegExp(this.getKeywords(funcs), 'gm'),     css: 'functions'    },
	{ regex: new RegExp(this.getKeywords(keywords), 'gm'),  css: 'keyword'      }
    ];

    this.forHtmlScript(SyntaxHighlighter.regexLib.phpScriptTags);
}

SyntaxHighlighter.brushes.OCaml.prototype  = new SyntaxHighlighter.Highlighter();
SyntaxHighlighter.brushes.OCaml.aliases  = ['ocaml', 'OCaml'];
