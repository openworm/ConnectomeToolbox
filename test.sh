set -ex

pip install .

##   Test readers

python -m cect.SpreadsheetDataReader 
python -m cect.UpdatedSpreadsheetDataReader                                                                                                                                                                      
python -m cect.UpdatedSpreadsheetDataReader2                                                                                                                                                                  
#python -m cect.OpenWormReader 



echo
echo "  Successfully completed all cect tests!"
echo
  

