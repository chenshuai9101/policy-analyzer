# 政策拆解分析器

## 一、Skill概述

- **名称**：policy-analyzer
- **版本**：v1.0
- **目标**：帮助创业者和求职者快速理解政策红利，降低政策信息获取门槛
- **核心价值**：信息差价值（政策红利不对称）+ 时效提醒（申报窗口期）+ 新政推送（第一时间获取）
- **目标用户**：创业者（企业主、个体工商户）、求职者（应届生、转行者）、HR/HRBP、政策申报专员

## 二、核心功能

### 2.1 政策检索（search_policy）

| 功能 | 说明 |
|------|------|
| 关键词搜索 | 支持政策名称、文号、关键词模糊匹配 |
| 地域筛选 | 国家/省/市/区四级筛选 |
| 行业匹配 | 科技类、制造类、服务类、农业类等 |
| 时间排序 | 按发布日期、截止日期排序 |
| 类型筛选 | 补贴类、税收优惠、人才引进、创业扶持等 |

**输入参数**：
```python
{
    "keywords": str,      # 搜索关键词
    "region": str,        # 地域范围：national/province/city
    "industry": str,      # 行业类型
    "policy_type": str,   # 政策类型
    "deadline_before": str # 截止日期筛选
}
```

**输出**：
```python
{
    "policies": [
        {
            "id": str,
            "title": str,
            "source": str,
            "publish_date": str,
            "deadline": str,
            "summary": str,
            "match_score": float
        }
    ],
    "total": int
}
```

### 2.2 政策解析（analyze_policy）

| 功能 | 说明 |
|------|------|
| 核心要点提取 | 政策核心内容提炼为3-5个要点 |
| 适用条件分析 | 列出申报条件、资格要求 |
| 申报流程梳理 | 时间线 + 所需材料清单 |
| 补贴额度计算 | 自动计算最高可申请金额 |
| 风险提示 | 不符合条件项、常见被拒原因 |

**输入参数**：
```python
{
    "policy_id": str,
    "user_profile": {
        "region": str,
        "industry": str,
        "company_type": str,  # 国有企业/民营企业/个体工商户
        "employee_count": int,
        "annual_revenue": float,
        "qualifications": list  # 已取得的资质证书
    }
}
```

**输出**：
```python
{
    "policy_id": str,
    "core_points": [str],        # 核心要点
    "eligibility": {
        "qualified": bool,
        "conditions": [str],
        "missing_items": [str]
    },
    "application_process": {
        "steps": [{"step": int, "action": str, "duration": str}],
        "materials": [str],
        "estimated_time": str
    },
    "subsidy_estimate": {
        "min": float,
        "max": float,
        "calculation_basis": str
    },
    "risk_alerts": [str]
}
```

### 2.3 个性化匹配（match_policy）

| 功能 | 说明 |
|------|------|
| 用户画像匹配 | 基于用户基本信息推荐最相关政策 |
| 资格预判 | 快速判断是否符合基本申报条件 |
| 成功率评估 | 基于历史数据评估申报成功率 |
| 优先级排序 | 按匹配度+补贴额度+时效性综合排序 |

**输入参数**：
```python
{
    "user_profile": {
        "region": str,
        "industry": str,
        "company_type": str,
        "employee_count": int,
        "annual_revenue": float,
        "qualifications": list,
        "business_age": int,      # 经营年限
        "is_high_tech": bool,    # 是否高新企业
        "is_small_micro": bool   # 是否小微企业
    },
    "focus_areas": [str],        # 关注的政策领域
    "limit": int                 # 返回数量限制
}
```

**输出**：
```python
{
    "matched_policies": [
        {
            "policy_id": str,
            "title": str,
            "match_score": float,        # 0-100
            "success_probability": float, # 0-100
            "estimated_subsidy": float,
            "urgency": str,               # high/medium/low
            "reasons": [str]              # 匹配原因说明
        }
    ],
    "total_matched": int,
    "recommendations": str           # 整体建议
}
```

### 2.4 时效提醒（get_reminders）

| 功能 | 说明 |
|------|------|
| 政策截止日期提醒 | 提前7/14/30天提醒 |
| 新政推送 | 实时监控最新政策发布 |
| 申报窗口期提醒 | 申报倒计时 + 错过风险提示 |
| 状态追踪 | 申报进度、结果查询 |

**输入参数**：
```python
{
    "user_id": str,
    "subscribed_policies": [str],
    "reminder_days": [int]  # 提前提醒天数
}
```

**输出**：
```python
{
    "reminders": [
        {
            "policy_id": str,
            "title": str,
            "deadline": str,
            "days_remaining": int,
            "urgency_level": str,
            "action_required": str
        }
    ],
    "new_policies": [str],  # 最新政策列表
    "warning_policies": [str]  # 即将截止的政策
}
```

## 三、核心数据结构

### 3.1 政策实体

```python
class Policy:
    policy_id: str           # 政策唯一标识
    title: str               # 政策标题
    source: str              # 发布来源
    source_url: str          # 原文链接
    region: str              # 适用地域
    industry: str            # 适用行业
    policy_type: str         # 政策类型
    publish_date: str        # 发布日期
    deadline: str            # 截止日期
    content: str             # 政策全文
    core_points: [str]       # 核心要点
    eligibility: [str]       # 申报条件
    materials: [str]         # 所需材料
    subsidy_info: dict       # 补贴信息
    application_steps: [dict] # 申报步骤
```

### 3.2 用户画像

```python
class UserProfile:
    user_id: str
    region: str
    industry: str
    company_type: str
    employee_count: int
    annual_revenue: float
    qualifications: [str]
    business_age: int
    is_high_tech: bool
    is_small_micro: bool
    contact_email: str
    subscribed_keywords: [str]
```

## 四、实现方案

### 4.1 政策库

| 层级 | 数据来源 | 更新频率 |
|------|----------|----------|
| 国家级 | 国务院、发改委、财政部官网 | 实时 |
| 省级 | 各省政务服务网 | 每日 |
| 市级 | 各地市政策文件库 | 每日 |
| 行业专项 | 工信部、科技部、人社部等 | 实时 |

### 4.2 解析引擎架构

```
用户输入 → 意图识别 → 政策检索 → 智能解析 → 匹配计算 → 结果输出
     ↓          ↓           ↓           ↓           ↓
  自然语言   分类模型     倒排索引    NLP提取     评分算法
```

**核心模块**：
1. **意图识别模块**：判断用户查询类型（检索/解析/匹配）
2. **检索模块**：基于Elasticsearch的全文检索
3. **解析模块**：使用NLP提取核心信息点
4. **匹配模块**：基于规则的资格判断 + 机器学习评分

### 4.3 评分算法

```python
def calculate_match_score(policy, user_profile):
    score = 0
    # 地域匹配 (20分)
    if policy.region == user_profile.region:
        score += 20
    elif policy.region == 'national':
        score += 15
    
    # 行业匹配 (25分)
    if policy.industry == user_profile.industry:
        score += 25
    elif policy.industry == 'general':
        score += 15
    
    # 资质匹配 (30分)
    qualification_match = len(set(policy.required_qualifications) & 
                              set(user_profile.qualifications))
    score += min(qualification_match * 10, 30)
    
    # 规模匹配 (15分)
    if is_scale_compatible(policy, user_profile):
        score += 15
    
    # 时效性 (10分)
    days_to_deadline = calculate_days(policy.deadline)
    if days_to_deadline > 30:
        score += 10
    elif days_to_deadline > 7:
        score += 5
    
    return score
```

## 五、API接口规范

### 5.1 搜索政策

```
POST /api/v1/policies/search
Content-Type: application/json

Request Body:
{
    "keywords": "科技型中小企业",
    "region": "广东省",
    "industry": "科技",
    "page": 1,
    "page_size": 10
}

Response:
{
    "code": 200,
    "message": "success",
    "data": {
        "policies": [...],
        "total": 156,
        "page": 1,
        "page_size": 10
    }
}
```

### 5.2 解析政策

```
POST /api/v1/policies/analyze
Content-Type: application/json

Request Body:
{
    "policy_id": "POL20240001",
    "user_profile": {...}
}
```

### 5.3 匹配政策

```
POST /api/v1/policies/match
Content-Type: application/json

Request Body:
{
    "user_profile": {...},
    "limit": 10
}
```

## 六、质量标准

### 6.1 准确性标准

| 指标 | 目标值 | 测量方法 |
|------|--------|----------|
| 政策检索准确率 | ≥85% | 抽样人工评估 |
| 匹配度评估准确率 | ≥80% | 历史申报数据验证 |
| 要点提取完整度 | ≥90% | 核心要点覆盖率 |
| 申报条件识别率 | ≥95% | 条件项遗漏检测 |

### 6.2 性能标准

| 指标 | 目标值 |
|------|--------|
| 单次检索响应时间 | <3秒 |
| 政策解析响应时间 | <15秒 |
| 批量匹配响应时间 | <30秒 |
| 系统可用性 | ≥99.5% |

### 6.3 用户满意度

| 指标 | 目标值 |
|------|--------|
| 整体满意度 | ≥4.2/5.0 |
| 政策实用性评分 | ≥4.0/5.0 |
| 信息准确度评分 | ≥4.5/5.0 |
| 响应速度评分 | ≥4.0/5.0 |

## 七、数据更新机制

### 7.1 更新策略

```
国家级政策: 实时监控 + 2小时内入库
省级政策: 每日增量更新
市级政策: 每日增量更新
历史政策: 归档处理 + 标记失效
```

### 7.2 失效检测

- 定期检查政策链接有效性
- 自动标记已过期政策
- 用户订阅过期提醒

## 八、安全与合规

- 所有政策数据来源于政府官方渠道
- 不存储敏感个人信息
- 政策解读仅供参考，以官方原文为准
- 数据加密传输（HTTPS）
- 定期安全审计

## 九、使用示例

### 示例1：创业者查找补贴政策

```python
# 用户输入
result = search_policy(
    keywords="创业补贴",
    region="深圳",
    industry="科技",
    policy_type="创业扶持"
)

# 返回匹配度最高的创业补贴政策列表
```

### 示例2：政策深度解析

```python
# 用户输入
result = analyze_policy(
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

# 返回详细解析报告，包含申报条件、所需材料、预估补贴金额
```

### 示例3：一键智能匹配

```python
# 用户输入
result = match_policy(
    user_profile={...},
    focus_areas=["补贴", "税收优惠", "人才引进"],
    limit=5
)

# 返回个性化政策推荐清单，按匹配度排序
```
