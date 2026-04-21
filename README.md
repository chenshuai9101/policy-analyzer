# 政策拆解分析器 (Policy Analyzer)

帮助创业者和求职者快速理解政策红利的智能分析工具。

## 核心价值

- **信息差价值**：政策红利不对称，快速获取竞争优势
- **时效提醒**：申报窗口期提醒，避免错过最佳申报时机
- **新政推送**：第一时间获取最新政策动态
- **智能匹配**：基于用户画像精准推荐最相关政策

## 功能特性

### 1. 政策检索
```python
from policy_engine import PolicySearchEngine

engine = PolicySearchEngine()
results = engine.search_policy(
    keywords="科技型中小企业",
    region="广东省",
    industry="科技",
    policy_type="创业扶持"
)
```

### 2. 政策深度解析
```python
from policy_engine import PolicyAnalyzer, PolicySearchEngine

engine = PolicySearchEngine()
analyzer = PolicyAnalyzer(engine)

analysis = analyzer.analyze_policy(
    policy_id="POL20240001",
    user_profile={
        "region": "深圳",
        "industry": "互联网",
        "company_type": "有限责任公司",
        "employee_count": 15,
        "annual_revenue": 5000000,
        "is_small_micro": True
    }
)
```

### 3. 智能匹配
```python
from policy_engine import PolicyMatcher, PolicySearchEngine

engine = PolicySearchEngine()
matcher = PolicyMatcher(engine)

recommendations = matcher.match_policy(
    user_profile={
        "region": "深圳",
        "industry": "科技",
        "employee_count": 50,
        "annual_revenue": 10000000,
        "is_small_micro": True
    },
    focus_areas=["补贴", "税收优惠", "人才引进"],
    limit=5
)
```

### 4. 时效提醒
```python
from policy_engine import PolicyReminder, PolicySearchEngine

engine = PolicySearchEngine()
reminder = PolicyReminder(engine)

alerts = reminder.get_reminders(
    reminder_days=[7, 14, 30]
)
```

## 安装

```bash
pip install -r requirements.txt
```

## 项目结构

```
policy-analyzer/
├── SKILL.md              # Skill定义文档
├── README.md             # 项目说明
├── requirements.txt      # 依赖包
└── scripts/
    └── policy_engine.py  # 核心引擎
```

## 目标用户

- 🚀 **创业者**：企业主、个体工商户寻找政策补贴
- 💼 **求职者**：应届生、转行者了解就业创业政策
- 👔 **HR/HRBP**：了解人才引进、培训补贴政策
- 📋 **政策申报专员**：提高申报效率和准确度

## 验收标准

| 指标 | 目标值 |
|------|--------|
| 政策检索准确率 | ≥85% |
| 匹配度评估准确率 | ≥80% |
| 用户满意度 | ≥4.2/5.0 |
| 单次检索响应时间 | <3秒 |

## 数据来源

- 国务院、发改委、财政部官网（国家级）
- 各省政务服务网（省级）
- 各地市政策文件库（市级）
- 工信部、科技部、人社部（行业专项）

## 免责声明

本工具提供的政策解读仅供参考，实际申报请以政府官方文件为准。

## License

MIT License
