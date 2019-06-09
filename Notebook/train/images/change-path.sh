ls $1*.xml | while read i; do
    echo "$i" | python change-path.py > "$i"_new
    rm "$i"
    mv "$i"_new "$i"
done
