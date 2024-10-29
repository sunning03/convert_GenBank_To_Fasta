首先需要下载biopython依赖包，否则会报错`ModuleNotFoundError: No module named 'Bio'`

`pip install biopython -i https://pypi.tuna.tsinghua.edu.cn/simple`

## Windows版使用

input_file后输入GenBank文件路径

output_file后输入所需Fasta文件路径，如果不指定 `output_file` 路径，默认情况下可以在当前目录下生成一个与GenBank文件同名的FASTA文件

## Linux版使用

`python convert_genbank_to_fasta.py <input_file> [output_file]`

其中<input_file>为输入的GenBank文件

[output_file]后输入所需Fasta文件路径，如果不指定 `output_file` 路径，默认情况下可以在当前目录下生成一个与GenBank文件同名的FASTA文件