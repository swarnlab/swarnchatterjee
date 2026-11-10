import json, os, datetime, urllib.parse, urllib.request
from pathlib import Path
key=os.environ.get("SERPAPI_KEY")
if not key: raise SystemExit("Missing SERPAPI_KEY GitHub Actions secret")
params=urllib.parse.urlencode({"engine":"google_scholar_author","author_id":"GyPrRgcAAAAJ","api_key":key})
req=urllib.request.Request("https://serpapi.com/search.json?"+params,headers={"User-Agent":"AcademicWebsiteMetrics/1.0"})
with urllib.request.urlopen(req,timeout=40) as resp: data=json.load(resp)
if data.get("error"): raise RuntimeError(data["error"])
rows=data.get("cited_by",{}).get("table",[])
values={}
for row in rows:
    for metric, record in row.items():
        if isinstance(record,dict) and record.get("all") is not None:
            values[metric.lower().replace("_","-")]=int(str(record["all"]).replace(",",""))
result={"citations":values.get("citations"),"h_index":values.get("h-index"),"i10_index":values.get("i10-index") or values.get("i10-index"),"updated_at":datetime.datetime.now(datetime.timezone.utc).isoformat()}
if result["citations"] is None or result["h_index"] is None: raise RuntimeError("Metrics missing from API response; preserving previous snapshot")
Path("data/scholar-metrics.json").write_text(json.dumps(result,indent=2)+"\n")
print(result)
