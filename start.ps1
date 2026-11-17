$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$postgresData = Join-Path $PSScriptRoot '.postgres'
$postgresControl = 'C:\Program Files\PostgreSQL\18\bin\pg_ctl.exe'
if (Test-Path -LiteralPath (Join-Path $postgresData 'PG_VERSION')) {
    & $postgresControl -D $postgresData status | Out-Null
    if ($LASTEXITCODE -ne 0) {
        & $postgresControl -D $postgresData -l (Join-Path $postgresData 'server.log') -o '-p 5433 -h 127.0.0.1' -w start
        if ($LASTEXITCODE -ne 0) { throw 'PostgreSQL не запустился' }
    }
}
& '.\.venv\Scripts\python.exe' manage.py runserver 127.0.0.1:8002
