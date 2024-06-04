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



echo
echo "  Successfully completed all cect tests!"
echo
  

