set -ex

pip install .

##   Test readers

python -m cect.SpreadsheetDataReader 
python -m cect.UpdatedSpreadsheetDataReader                                                                                                                                                                      
python -m cect.UpdatedSpreadsheetDataReader2                                                                                                                                                                  
#python -m cect.OpenWormReader                                                                                                                                                            
python -m cect.VarshneyDataReader
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



echo
echo "  Successfully completed all cect tests!"
echo
  

