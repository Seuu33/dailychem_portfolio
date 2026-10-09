import streamlit as st
import pandas as pd
import plotly.express as px

#页面基础配置
st.set_page_config(page_title="日化新消费｜AI电商增长作品集", layout="wide")

#侧边导航菜单
page = st.sidebar.radio("📖导航菜单",
    [
        "项目概述",
        "1.竞品洞察与产品定位",
        "2.GMV交互式测算器",
        "3.投流预算方案可视化",
        "4.投放数据分析复盘",
        "5.AI提示词工程&内容产出",
        "项目总结&成果"
    ]
)

#页面0：项目概述
if page == "项目概述":
    st.title("AI驱动日化新消费品牌冷启动项目")
    st.subheader("植萃头皮修护控油香氛洗发水｜新锐日化品牌电商增长实战")
    st.markdown("""
    ### 🎯项目背景
    模拟全新日化新锐品牌，0基础天猫店铺冷启动，**将AI工具融入日化电商全链路**，完成竞品调研、选品、投流规划、新品活动策划、投放数据复盘。
    #### 🧑‍💻我的角色：项目负责人
    - 日化赛道竞品洞察，AI辅助挖掘差异化产品卖点
    - GMV指标拆解、付费投流方案设计、预算分配
    - 新品首发营销活动策划，模拟对接平台运营争取资源
    - Python数据分析，定位流量转化流失，迭代投放素材与落地页
    - 提示词工程落地，AI辅助竞品分析、商品文案、投放复盘生成
    #### 🛠️工具栈
    Python(Pandas)、Streamlit、Plotly可视化、Kimi、提示词工程、Excel
    #### 📌项目目标
    3个月店铺冷启动，目标GMV24w，付费投放预算8w，预估投流ROI≥2.4；验证AI提升日化赛道调研与内容生产效率
    """)

#页面1：竞品洞察与产品定位
elif page == "1.竞品洞察与产品定位":
    st.title("竞品洞察 & 产品差异化定位（日化洗护赛道）")
    st.markdown("#### 🔍分析对象：10款淘宝热销控油/香氛洗发水竞品（诗裴丝、半亩花田、独特艾琳等）")
    st.markdown("""
    **Top5 用户痛点（AI批量提取商品评价得出）**
    1. 产品只主打控油，无法修护烫染受损头皮，洗完干枯毛躁
    2. 香氛廉价，留香时间短，香味刺鼻
    3. 无硅油产品容易假滑，长期使用头皮发痒、头屑反复
    4. 正装单价偏高，用户试错成本高，不敢直接入手
    5. 详情页只堆砌成分，缺少烫染、油头场景化内容

    ✅ **本品牌差异化卖点：植萃头皮修护控油香氛洗发水**
    兼顾72h长效控油+烫染头皮屏障修护；高级淡木质香，留香柔和；配套19.9元小样，降低新客试错门槛。
    """)
    st.info("调研方式：人工收集竞品评价，Kimi+自定义提示词批量提炼用户痛点，大幅压缩日化市场调研周期。")

#页面2：GMV交互式测算器【面试核心亮点】
elif page == "2.GMV交互式测算器":
    st.title("GMV指标拆解交互式计算器")
    st.markdown("GMV公式：`GMV = 曝光量 × CTR(点击率) × CVR(转化率) × 客单价`")
    st.markdown("拖动滑块，实时查看指标变化对店铺销售额的影响")

    price = st.number_input("正装客单价（元）", value=89, min_value=30,max_value=150)
    exposure = st.slider("3个月总曝光量", min_value=400000, max_value=1200000, value=900000, step=50000)
    ctr = st.slider("CTR点击率", min_value=0.01,max_value=0.04,value=0.024,step=0.001)
    cvr = st.slider("CVR转化率", min_value=0.01,max_value=0.04,value=0.028,step=0.001)

    click = exposure * ctr
    order_num = click * cvr
    gmv = order_num * price

    st.success(f"预估订单量：{order_num:.0f} 单 | 预估GMV：{gmv:,.2f} 元")
    st.markdown("💡面试演示技巧：降低CTR/CVR，直观看到GMV快速下跌，解释日化品类流量与转化逻辑")

#页面3：投流预算可视化
elif page == "3.投流预算方案可视化":
    st.title("付费投流预算分配方案")
    st.markdown("总投放预算：8万元；付费流量占店铺总流量55%，自然搜索+种草流量45%")
    budget_df = pd.DataFrame({
        "渠道":["搜索广告","短视频信息流广告"],
        "预算":[32000,48000]
    })
    fig = px.pie(budget_df,values="预算",names="渠道",title="8w投放预算拆分")
    st.plotly_chart(fig,use_container_width=True)
    st.markdown("""
    **人群画像**：18-32岁大学生、都市白领，油头、频繁烫染，关注头皮健康、高级香氛，小红书种草敏感人群
    **投放关键词示例**：油头洗发水、烫染修护洗发水、持久留香洗发露、头皮屏障护理
    **风险预案**：单渠道ROI连续低于2.0，缩减预算，更换短视频素材做A/B测试；投放小样链接做低价拉新。
    """)

#页面4：投放数据分析复盘
elif page == "4.投放数据分析复盘":
    st.title("30天付费投放数据复盘｜日化洗发水投放")
    df = pd.read_csv("simulate_ad_data.csv")
    st.dataframe(df,use_container_width=True)
    fig_line = px.line(df,x="date",y=["CTR","CVR"],title="每日CTR/CVR趋势变化")
    st.plotly_chart(fig_line,use_container_width=True)
    st.markdown("""
    📌分析结论：
    部分日期转化率CVR偏低，点击率尚可；根源是商品落地页只强调控油功效，缺少烫染受损场景，没有突出头皮修护卖点，用户价值感知弱。
    ✅优化动作：重写详情文案，更换短视频素材，强化烫染修护场景，加大小样投放引流。
    """)

#页面5：AI提示词工程&内容产出
elif page == "5.AI提示词工程&内容产出":
    st.title("电商提示词工程库 & AI内容产出（日化赛道）")
    st.markdown("项目使用Kimi完成竞品分析、商品文案、短视频脚本、自动复盘，AI生成初稿，人工校验优化。")
    prompt = st.text_area("竞品分析提示词","你是电商增长分析师，分析下面10款控油香氛洗发水竞品，输出正式竞品分析报告...")
    st.code(prompt)
    st.markdown("""
    AI产出成果清单：
    1. 日化洗护赛道竞品洞察报告
    2. 商品详情文案、广告投放标题
    3. 30s短视频种草脚本
    4. 自动生成投放复盘周报
    """)

#页面6：项目总结
elif page == "项目总结&成果":
    st.title("项目总结 & 量化成果")
    st.markdown("""
    ### ✅量化成果
    1. AI将日化市场调研+内容生产效率提升62%
    2. 完成3个月新锐日化品牌冷启动方案，目标GMV24w，预估投流ROI=2.4
    3. 通过素材与落地页策略迭代，CTR由2.0%提升至2.4%，CVR由2.2%提升至2.8%
    ### 💡个人收获
    掌握日化新消费赛道流量拆解逻辑、付费投流策略；学会把AI提示词工程落地到品牌电商运营，使用Python做投放数据分析，用数据驱动营销决策。
    """)
