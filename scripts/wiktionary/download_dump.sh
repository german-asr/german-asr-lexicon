out_file=$1

if [[ -f $out_file ]]; then
    echo "Wiktionary Dump already downloaded"
else
    echo "Download Wiktionary Dump"
    version=20191120
    url=https://dumps.wikimedia.org/dewiktionary/${version}/dewiktionary-${version}-pages-articles-multistream.xml.bz2

    # download
    wget -O $out_file  $url

    # decompress
    bzip2 -d $out_file
fi
