from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Scatter


def scatter_base() -> Scatter:
    c = (
        Scatter()
        .add_xaxis(Faker.choose())
        .add_yaxis("商家A", Faker.values())
        .set_global_opts(title_opts=opts.TitleOpts(title="Scatter-基本示例"))
    )
    return c

scatter_base().render()