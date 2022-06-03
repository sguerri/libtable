from libtable import BaseTableData


def get_data():
    data = BaseTableData()
    data.add_header("iid", "IID", width=5, rightalign=True)
    data.add_header("title", "TITLE")
    data.add_header("desc", "DESC", weight=2)
    data.rows = [
        {
            "iid": "1",
            "title": "<b>AAA</b> <i>BBB</i>",
            "desc": "Description of AAA"
        },
        {
            "iid": "2",
            "title": "BBB dsqd qsd qd qdq q dqs",
            "desc": "<aaa bg='red'>Description of BBB</aaa>"
        },
        {
            "iid": "3",
            "title": 23,
            "desc": False
        },
        {
            "iid": "5",
            "title": "DDD",
            "desc": "<aaa bg='blue'>Description of DDD</aaa>"
        },
        {
            "iid": "15",
            "title": "EEE"
        }
    ]
    return data
