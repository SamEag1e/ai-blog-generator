$keyword = "wireless earbuds"
$encodedKeyword = [System.Web.HttpUtility]::UrlEncode($keyword)
$url = "http://localhost:5000/generate?keyword=$encodedKeyword"
$outputFile = "generated/$(Get-Date -Format yyyy-MM-dd).json"

Invoke-RestMethod -Uri $url -OutFile $outputFile
