import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from process_data import get_chart
app = dash.Dash()
#app.layout = html.Div(html.H6("Phung Tuan Hung"),className ='page main-title')
##css3###
main_item = {'margin':'20px','color':'#0803f8'}
server = app.server
app.layout = html.Div([

                        html.Div([
                                html.Img(src=app.get_asset_url("company_color_bar.PNG"),className='color_bar twelve columns')
                                ],className='twelve columns'),
                        html.Div([

                                    html.Div(html.Img(src=app.get_asset_url('bosch_logo.PNG'),className='Logo')
                                        ,className='two columns'),
                                    html.Div(html.H1(children='C/TXF-C1 MONTHLY KPI REPORT')
                                        ,className='ten columns',style={'float': 'right','text-align': 'center'}) #'margin-right':'40px'
                                ],className='display_in_line'),

                        html.H2(children='1. P94 Worklist Overview:',style=main_item),

                        html.Div([
                                    #chart left#
                                    html.Div([
                                        dcc.Graph(
                                            id="Price_chart",
                                            figure=get_chart.Trigger_logical_group(app)),
                                    ],className='six columns'),
                                    #chart right#
                                    html.Div([],className='six columns')
                                 ],className="display_in_line"),

                        html.Footer(html.Div([
                                html.Img(src=app.get_asset_url("company_color_bar.PNG"),className='color_bar twelve columns')
                                ],className='twelve columns Footer'))
                        ],className ='page') #
if __name__ == '__main__':
    app.run_server()
