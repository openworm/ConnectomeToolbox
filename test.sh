set -ex

ruff format cect/*
ruff check cect/*

pip install .[docs]

quick_test=0

if [[ ($# -eq 1) && ($1 == '-q') ]]; then
    quick_test=1
fi

##   Test readers
                                                                                                                    
python -m cect.Cells $quick_test
                                                                                                                                          
python -m cect.TestDataReader -nogui                                                                                                                                         
python -m cect.ConnectomeView                                                                                                                             
python -m cect.ConnectomeDataset -nogui

if [ "$quick_test" == 0 ]; then

    # Note: all run when Cells above called...
    
    #python -m cect.Cook2019DataReader
    #python -m cect.Cook2019HermReader -nogui
    #python -m cect.WormNeuroAtlasReader -nogui
    #python -m cect.WitvlietDataReader1
    #python -m cect.WitvlietDataReader2
    #python -m cect.WhiteDataReader
    #python -m cect.White_A
    #python -m cect.White_L4

    #python -m cect.Comparison 0
    
fi

mkdocs build

echo
echo "  Successfully completed all cect tests (quick run: $quick_test)!"
echo
  

