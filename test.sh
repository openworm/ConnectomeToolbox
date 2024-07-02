set -ex

pip install .

quick_test=false

if [[ ($# -eq 1) && ($1 == '-q') ]]; then
    quick_test=true
fi

##   Test readers

python -m cect.SpreadsheetDataReader 
python -m cect.UpdatedSpreadsheetDataReader                                                                                                                                                                      
python -m cect.UpdatedSpreadsheetDataReader2                                                                                                                                                                  
#python -m cect.OpenWormReader                                                                                                                                                            
python -m cect.VarshneyDataReader

if [ "$quick_test" == false ]; then

    python -m cect.Cook2019DataReader
    python -m cect.Cook2019HermReader
    python -m cect.WormNeuroAtlasReader
    python -m cect.W_SpreadsheetDataReader
    python -m cect.WitvlietDataReader1
    python -m cect.WitvlietDataReader2
    python -m cect.WhiteDataReader
    python -m cect.White_A
    python -m cect.White_L4
    python -m cect.White_whole
fi

python cect/Comparison.py $quick_test
mkdocs build

echo
echo "  Successfully completed all cect tests (quick run: $quick_test)!"
echo
  

