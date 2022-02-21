# Table Extractor

This is a wrapper for the [camelot][1] module. It can extract tabular information from PDF files. This is simply a wrapper that uses [click][2] for a CLI application. Essentially, call the CLI app, specify the list of PDFs and the export options.

[1]: https://camelot-py.readthedocs.io/en/master/
[2]: https://click.palletsprojects.com/en/8.0.x/


To list the number of tables it can see in a pdf:

```bash
$ te extract ./data/foo.pdf ./data/foo2.pdf
```

Extract the table data to CSV and Excel to the same folder as the pdf:

```bash
$ te extract ./data/foo.pdf --export=csv --export=excel
```


You can compress the output into a zip file using the `--compress` switch:

```bash
$ te extract ./data/foo.pdf --export=csv --compress
```

>NOTE: The `--compress` switch is really only suitable for one export type as it will create a zip file named after the PDF file and overwrite any other export option.


Extract table data from particular pages:

```bash
$ te extract ./data/foo.pdf --export=csv --export=excel --pages='75-85'
```

Export from multiple PDF files to multiple formats:

```bash
$ te extract ./data/foo.pdf ./data/foo2.pdf --export=csv --export=excel
```

The available export options are:

- csv 
- excel 
- html 
- json 
- markdown 
- sqlite


```bash
$ te extract ./data/foo.pdf --export=csv --export=excel --export=html --export=json --export=markdown --export=sqlite
```


## License

[MIT](https://choosealicense.com/licenses/mit/)

