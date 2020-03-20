CWD=`pwd`

SCRIPTDIR="$(dirname "$0")" >/dev/null 2>&1;
cd $SCRIPTDIR
make html

cd $CWD
