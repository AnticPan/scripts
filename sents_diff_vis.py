import csv

TEMPLATE = """<!DOCTYPE html>
<html lang="">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>
    <header></header>
    <main>
        <table border="1">
        %s
        </table>
    </main>
    <footer></footer>
  </body>
</html>"""

def get_lcs(s1, s2):
    dp = [[0]*(len(s2) + 1) for _ in range(len(s1)+1)]
    for x in range(1, len(s1)+1):
        for y in range(1, len(s2)+1):
            if s1[x-1] == s2[y-1]:
                dp[x][y] = dp[x-1][y-1] + 1
            else:
                dp[x][y] = max(dp[x-1][y], dp[x][y-1])

    x, y = len(s1), len(s2)
    lcs=[]
    while dp[x][y]:
        if dp[x][y] == dp[x-1][y-1]+1:
            lcs.append(s1[x-1])
            x-=1
            y-=1
        elif dp[x][y] == dp[x][y-1]:
            x-=1
        elif dp[x][y] == dp[x-1][y]:
            y-=1
    return lcs[::-1]

def mark(s, lcs):
    out = ""
    lcs_ptr = 0
    diff = ""
    for w in s:
        if lcs_ptr < len(lcs) and w == lcs[lcs_ptr]:
            if diff:
                out += '<text style="color:red;">'+ diff+ '</text>'
                diff = ""
            out += w + " "
            lcs_ptr += 1
        else:
            diff += w + " "
    if diff:
        out += '<text style="color:red;">'+ diff+ '</text>'
    return "<td>"+out+"</td>"

def to_html_cell(idx, pair):
    x,y = pair
    lcs = get_lcs(x,y)
    x_html = mark(x,lcs)
    y_html = mark(y,lcs)
    return f"<tr>\n<td>{idx}&emsp;</td>\n{x_html}\n{y_html}</tr>\n"


if __name__ == "__main__":
    file_name = 'samples/test.csv'
    out_name = "samples/diff_vis.%d.html"
    block_size = 5000

    pairs = []
    with open(file_name, encoding="utf-8") as f:
        reader = csv.reader(f)
        for i, line in enumerate(reader):
            x, y = line
            pairs.append((x.split(), y.split()))

    content = ""
    file_idx = 0
    for idx, pair in enumerate(pairs):
        content += to_html_cell(idx+1, pair)
        if (idx+1)%block_size==0 or idx==len(pairs)-1:
            html = TEMPLATE%content
            content = ""
            with open(out_name%file_idx,"w", encoding='utf-8') as f:
                f.write(html)
                file_idx += 1
