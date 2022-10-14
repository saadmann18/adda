FILES="*.ply"
for f in $FILES
do
  echo "Processing $f file..."
  # take action on each file. $f store current file name
  re=${f%%.*}
  echo "$re"
  python ply2obj.py $f
  cat "$f"
done
