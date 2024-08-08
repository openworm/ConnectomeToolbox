set -ex

pip install .[docs]

quick_test=0

if [[ ($# -eq 1) && ($1 == '-q') ]]; then
    quick_test=1
fi

##   Test readers
                                                                                                                       
python -m cect.Cells
python -m cect.SpreadsheetDataReader 
python -m cect.UpdatedSpreadsheetDataReader                                                                                                                                                                      
python -m cect.UpdatedSpreadsheetDataReader2                                                                                                                                                                  
#python -m cect.OpenWormReader                                                                                                                                                            
python -m cect.VarshneyDataReader
python -m cect.Cook2020DataReader       
python -m cect.White_whole   -nogui                                                                                                                                              
python -m cect.TestDataReader -nogui                                                                                                                                         
python -m cect.ConnectomeView                                                                                                                                   
python -m cect.ConnectomeDataset

if [ "$quick_test" == 0 ]; then

    python -m cect.Cook2019DataReader
    python -m cect.Cook2019HermReader
    python -m cect.WormNeuroAtlasReader
    python -m cect.W_SpreadsheetDataReader
    python -m cect.WitvlietDataReader1
    python -m cect.WitvlietDataReader2
    python -m cect.WhiteDataReader
    python -m cect.White_A
    python -m cect.White_L4
fi

python cect/Comparison.py $quick_test
mkdocs build

echo
echo "  Successfully completed all cect tests (quick run: $quick_test)!"
echo
  

