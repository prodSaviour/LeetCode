# Read from the file file.txt and print its transposed content to stdout.
awk '
{
    for (i = 1; i <= NF; i++)
        a[NR, i] = $i
}
NF > p { p = NF }
END {
    for (i = 1; i <= p; i++) {
        for (j = 1; j <= NR; j++)
            printf "%s%s", a[j, i], (j == NR ? "" : " ")
        print ""
    }
}' file.txt