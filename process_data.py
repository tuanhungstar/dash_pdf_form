import pandas as pd
import plotly.graph_objects as go
findlink ="D:/python/Dash Plotly/dash pdf form/data/MASTER_UPDATE.xlsx"


class get_chart:
    def Trigger_logical_group(app):

        wl_p94_lg_AI = pd.read_excel(findlink,'AI_FUNCTION_PER_GROUP')
        labels = wl_p94_lg_AI['Input_#4_Logical Group']
        values = wl_p94_lg_AI['Total Parts']
        colors = ['gold', 'mediumturquoise', 'darkorange']
        fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig.update_traces(title=dict(text="Triggered By Logical Group", font=dict(size=18)),hoverinfo='label+percent', textinfo='label+value', textfont_size=20,showlegend=False,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
        return fig
