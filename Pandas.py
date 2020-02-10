import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('mysql+pymysql://root:@localhost/test')
df = pd.read_sql_table('links', engine)
print(df.head())

# for PyMySQL
# engine = create_engine('mysql+pymysql://root:@localhost/test')

def color_negative_red(value):
    if value < 0:
        color = 'red'
    elif value > 0:
        color = 'green'
    else:
        color = 'black'

    return 'color: %s' % color


Premier_league = df.style.applymap(color_negative_red, subset=['GD'])


def magnify():
    return [dict(selector="th",
                 props=[("font-size", "5pt")]),
            dict(selector="td",
                 props=[('padding', "0.5em 0.5em")]),
            dict(selector="th:hover",
                 props=[("font-size", "10pt")]),
            dict(selector="tr:hover td:hover",
                 props=[('max-width', '500px'),
                        ('font-size', '12pt')])
            ]


Premier_league.set_table_styles(magnify())