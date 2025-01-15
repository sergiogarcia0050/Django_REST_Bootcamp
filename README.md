expresión regular que borra los pyc y migraciones:

Get-ChildItem -Recurse -File |
     Where-Object {
         (
             $_.FullName -match "migrations" -and 
             $_.Name -ne "__init__.py" -and
             $_.FullName -notmatch '(\\|/)env(\\|/)'
         ) -or
         (    
             $_.FullName -match '^((?!\\env\\).)*\.(pyc|pyo|log)$'
         )
     } |  
     Remove-Item -Force
