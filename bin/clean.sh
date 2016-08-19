ROOT=$1
TO_FIND=$2

find $ROOT -iname $TO_FIND -exec rm -rf {} +
