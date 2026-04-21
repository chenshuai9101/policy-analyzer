"""
政策拆解分析器 - 核心引擎
提供政策检索、解析、匹配等功能
"""

import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class Policy:
    """政策实体"""
    policy_id: str
    title: str
    source: str
    source_url: str
    region: str
    industry: str
    policy_type: str
    publish_date: str
    deadline: str
    content: str
    core_points: List[str] = field(default_factory=list)
    eligibility: List[str] = field(default_factory=list)
    materials: List[str] = field(default_factory=list)
    subsidy_info: Dict[str, Any] = field(default_factory=dict)
    application_steps: List[Dict] = field(default_factory=list)


@dataclass
class UserProfile:
    """用户画像"""
    region: str
    industry: str
    company_type: str
    employee_count: int = 0
    annual_revenue: float = 0.0
    qualifications: List[str] = field(default_factory=list)
    business_age: int = 0
    is_high_tech: bool = False
    is_small_micro: bool = False
    focus_areas: List[str] = field(default_factory=list)


class PolicySearchEngine:
    """政策搜索引擎"""
    
    def __init__(self):
        self.policies: List[Policy] = []
        self._init_sample_policies()
    
    def _init_sample_policies(self):
        """初始化示例政策数据"""
        self.policies = [
            Policy(
                policy_id="POL20240001",
                title="科技型中小企业技术创新基金",
                source="科技部",
                source_url="https://www.most.gov.cn/",
                region="national",
                industry="科技",
                policy_type="创业扶持",
                publish_date="2024-01-15",
                deadline="2024-12-31",
                content="支持科技型中小企业开展技术创新活动...",
                core_points=[
                    "最高资助金额200万元",
                    "重点支持高新技术领域",
                    "无偿资助+股权投资结合",
                    "优先支持省级以上科技企业孵化器在孵企业"
                ],
                eligibility=[
                    "在中国境内注册的居民企业",
                    "职工总数不超过500人",
                    "年销售收入不超过2亿元",
                    "资产总额不超过2亿元",
                    "不属于上市企业"
                ],
                materials=[
                    "企业营业执照",
                    "上年度财务报表",
                    "研发项目计划书",
                    "知识产权证明",
                    "科技人员名单"
                ],
                subsidy_info={"min": 20, "max": 200, "unit": "万元", "type": "无偿资助"},
                application_steps=[
                    {"step": 1, "action": "网上注册申报", "duration": "3个工作日"},
                    {"step": 2, "action": "地方科技部门初审", "duration": "10个工作日"},
                    {"step": 3, "action": "科技部评审", "duration": "20个工作日"},
                    {"step": 4, "action": "立项公示", "duration": "5个工作日"},
                    {"step": 5, "action": "签订合同", "duration": "7个工作日"}
                ]
            ),
            Policy(
                policy_id="POL20240002",
                title="小微企业税收优惠政策",
                source="财政部 税务总局",
                source_url="https://www.mof.gov.cn/",
                region="national",
                industry="general",
                policy_type="税收优惠",
                publish_date="2024-01-01",
                deadline="2027-12-31",
                content="对月销售额10万元以下的小规模纳税人免征增值税...",
                core_points=[
                    "增值税小规模纳税人起征点提高至月销售额10万元",
                    "小型微利企业企业所得税优惠",
                    "六税两费减半征收",
                    "研发费用加计扣除比例提高至100%"
                ],
                eligibility=[
                    "增值税小规模纳税人",
                    "小型微利企业：年应纳税所得额≤300万元、从业人数≤300人、资产总额≤5000万元"
                ],
                materials=[
                    "税务登记证",
                    "财务报表",
                    "从业人数证明",
                    "资产总额证明"
                ],
                subsidy_info={"min": 0, "max": 0, "unit": "万元", "type": "税收减免", "tax_types": ["增值税", "企业所得税", "六税两费"]},
                application_steps=[
                    {"step": 1, "action": "税务登记确认", "duration": "即时"},
                    {"step": 2, "action": "优惠备案", "duration": "1个工作日"},
                    {"step": 3, "action": "自动享受优惠", "duration": "申报时自动计算"}
                ]
            ),
            Policy(
                policy_id="POL20240003",
                title="深圳市创业担保贷款贴息政策",
                source="深圳市人社局",
                source_url="https://hrss.sz.gov.cn/",
                region="深圳市",
                industry="general",
                policy_type="创业扶持",
                publish_date="2024-03-01",
                deadline="2024-12-31",
                content="为符合条件的创业者提供贴息贷款支持...",
                core_points=[
                    "个人创业担保贷款最高50万元",
                    "小微企业贷款最高500万元",
                    "贴息比例LPR-150BP",
                    "最长期限3年"
                ],
                eligibility=[
                    "重点就业群体：高校毕业生、登记失业人员、退役军人等",
                    "或为上述人员创办的小微企业",
                    "企业正常经营满6个月",
                    "无不良信用记录"
                ],
                materials=[
                    "身份证件",
                    "营业执照",
                    "经营场所证明",
                    "就业创业证",
                    "还款能力证明"
                ],
                subsidy_info={"min": 0, "max": 50, "unit": "万元/人", "type": "贷款贴息"},
                application_steps=[
                    {"step": 1, "action": "网上申请", "duration": "1个工作日"},
                    {"step": 2, "action": "材料审核", "duration": "5个工作日"},
                    {"step": 3, "action": "银行审批", "duration": "10个工作日"},
                    {"step": 4, "action": "签订合同", "duration": "3个工作日"}
                ]
            ),
            Policy(
                policy_id="POL20240004",
                title="高层次人才引进计划",
                source="广东省人社厅",
                source_url="https://hrss.gd.gov.cn/",
                region="广东省",
                industry="general",
                policy_type="人才引进",
                publish_date="2024-02-01",
                deadline="2024-10-31",
                content="引进培育高层次创新创业人才...",
                core_points=[
                    "安家补贴最高500万元",
                    "科研启动经费最高1000万元",
                    "住房保障、子女入学优待",
                    "人才绿卡一卡通服务"
                ],
                eligibility=[
                    "海外留学归国人员",
                    "博士学位获得者",
                    "具有副高级以上专业技术职称",
                    "或符合条件的创新创业团队核心成员"
                ],
                materials=[
                    "身份证件、学历学位证书",
                    "专业技术资格证书",
                    "工作经历证明",
                    "业绩成果证明材料",
                    "引进单位证明"
                ],
                subsidy_info={"min": 50, "max": 1500, "unit": "万元", "type": "综合性人才支持"},
                application_steps=[
                    {"step": 1, "action": "个人申请", "duration": "5个工作日"},
                    {"step": 2, "action": "单位审核", "duration": "3个工作日"},
                    {"step": 3, "action": "专家评审", "duration": "20个工作日"},
                    {"step": 4, "action": "公示认定", "duration": "10个工作日"},
                    {"step": 5, "action": "签订协议", "duration": "7个工作日"}
                ]
            ),
            Policy(
                policy_id="POL20240005",
                title="专精特新企业培育计划",
                source="工信部",
                source_url="https://www.miit.gov.cn/",
                region="national",
                industry="制造业",
                policy_type="企业培育",
                publish_date="2024-01-20",
                deadline="2024-11-30",
                content="培育一批专注于细分市场、创新能力强、成长性好的专精特新企业...",
                core_points=[
                    "认定为专精特新企业",
                    "最高奖励100万元",
                    "优先推荐申报国家项目",
                    "享受金融支持服务"
                ],
                eligibility=[
                    "依法在境内登记注册的中小企业",
                    "上年度营业收入1000万元以上",
                    "近两年研发投入占比≥3%",
                    "拥有自主知识产权或独特竞争优势"
                ],
                materials=[
                    "企业基本情况表",
                    "近两年财务审计报告",
                    "研发投入证明",
                    "知识产权证书",
                    "主导产品说明"
                ],
                subsidy_info={"min": 20, "max": 100, "unit": "万元", "type": "认定奖励"},
                application_steps=[
                    {"step": 1, "action": "网上填报", "duration": "3个工作日"},
                    {"step": 2, "action": "地方推荐", "duration": "10个工作日"},
                    {"step": 3, "action": "专家评审", "duration": "30个工作日"},
                    {"step": 4, "action": "公示认定", "duration": "15个工作日"}
                ]
            )
        ]
    
    def search_policy(
        self,
        keywords: str = "",
        region: str = "",
        industry: str = "",
        policy_type: str = "",
        deadline_before: str = ""
    ) -> Dict[str, Any]:
        """
        政策检索
        
        Args:
            keywords: 搜索关键词
            region: 地域筛选
            industry: 行业筛选
            policy_type: 政策类型
            deadline_before: 截止日期筛选
        
        Returns:
            符合条件的政策列表
        """
        results = []
        
        for policy in self.policies:
            # 关键词匹配
            if keywords:
                if keywords.lower() not in policy.title.lower() and \
                   keywords.lower() not in policy.content.lower():
                    continue
            
            # 地域筛选
            if region:
                if region not in policy.region and policy.region != "national":
                    continue
            
            # 行业筛选
            if industry:
                if industry not in policy.industry and policy.industry != "general":
                    continue
            
            # 类型筛选
            if policy_type:
                if policy_type not in policy.policy_type:
                    continue
            
            # 截止日期筛选
            if deadline_before:
                try:
                    deadline_dt = datetime.strptime(policy.deadline, "%Y-%m-%d")
                    before_dt = datetime.strptime(deadline_before, "%Y-%m-%d")
                    if deadline_dt > before_dt:
                        continue
                except ValueError:
                    pass
            
            # 计算匹配得分
            match_score = self._calculate_search_score(policy, keywords, region, industry)
            
            results.append({
                "id": policy.policy_id,
                "title": policy.title,
                "source": policy.source,
                "publish_date": policy.publish_date,
                "deadline": policy.deadline,
                "summary": " | ".join(policy.core_points[:2]),
                "match_score": match_score,
                "region": policy.region,
                "industry": policy.industry,
                "policy_type": policy.policy_type
            })
        
        # 按匹配度排序
        results.sort(key=lambda x: x["match_score"], reverse=True)
        
        return {
            "policies": results,
            "total": len(results)
        }
    
    def _calculate_search_score(self, policy: Policy, keywords: str, region: str, industry: str) -> float:
        """计算搜索匹配得分"""
        score = 50.0  # 基础分
        
        # 关键词匹配加分
        if keywords:
            if keywords in policy.title:
                score += 30
            if keywords in policy.core_points:
                score += 10
        
        # 地域匹配加分
        if region:
            if region in policy.region:
                score += 15
            elif policy.region == "national":
                score += 10
        
        # 行业匹配加分
        if industry:
            if industry in policy.industry:
                score += 15
            elif policy.industry == "general":
                score += 5
        
        return round(score, 2)


class PolicyAnalyzer:
    """政策解析器"""
    
    def __init__(self, search_engine: PolicySearchEngine):
        self.search_engine = search_engine
    
    def analyze_policy(self, policy_id: str, user_profile: Dict) -> Dict[str, Any]:
        """
        政策深度解析
        
        Args:
            policy_id: 政策ID
            user_profile: 用户画像
        
        Returns:
            详细解析报告
        """
        # 查找政策
        policy = None
        for p in self.search_engine.policies:
            if p.policy_id == policy_id:
                policy = p
                break
        
        if not policy:
            return {"error": "政策不存在", "policy_id": policy_id}
        
        # 构建用户画像对象
        profile = UserProfile(
            region=user_profile.get("region", ""),
            industry=user_profile.get("industry", ""),
            company_type=user_profile.get("company_type", ""),
            employee_count=user_profile.get("employee_count", 0),
            annual_revenue=user_profile.get("annual_revenue", 0),
            qualifications=user_profile.get("qualifications", []),
            business_age=user_profile.get("business_age", 0),
            is_high_tech=user_profile.get("is_high_tech", False),
            is_small_micro=user_profile.get("is_small_micro", False)
        )
        
        # 分析资格匹配
        eligibility_analysis = self._analyze_eligibility(policy, profile)
        
        # 估算补贴金额
        subsidy_estimate = self._estimate_subsidy(policy, profile)
        
        # 生成风险提示
        risk_alerts = self._generate_risk_alerts(policy, profile)
        
        # 估算总申报时间
        estimated_time = self._calculate_total_time(policy)
        
        return {
            "policy_id": policy.policy_id,
            "title": policy.title,
            "source": policy.source,
            "core_points": policy.core_points,
            "eligibility": eligibility_analysis,
            "application_process": {
                "steps": policy.application_steps,
                "materials": policy.materials,
                "estimated_time": estimated_time
            },
            "subsidy_estimate": subsidy_estimate,
            "risk_alerts": risk_alerts,
            "urgency": self._assess_urgency(policy.deadline)
        }
    
    def _analyze_eligibility(self, policy: Policy, profile: UserProfile) -> Dict[str, Any]:
        """分析资格匹配情况"""
        qualified_conditions = []
        missing_items = []
        
        # 检查地域
        if profile.region in policy.region or policy.region == "national":
            qualified_conditions.append(f"✓ 地域匹配：{policy.region}")
        else:
            missing_items.append(f"✗ 地域要求：仅限{policy.region}")
        
        # 检查行业
        if profile.industry in policy.industry or policy.industry == "general":
            qualified_conditions.append(f"✓ 行业匹配：{policy.industry}")
        else:
            missing_items.append(f"✗ 行业要求：{policy.industry}类企业")
        
        # 检查企业规模
        if policy.policy_type == "税收优惠":
            if profile.is_small_micro:
                qualified_conditions.append("✓ 小微企业认定")
            elif profile.employee_count <= 300 and profile.annual_revenue <= 5000:
                qualified_conditions.append("✓ 符合小微企业标准")
            else:
                missing_items.append("需满足小微企业标准")
        
        # 检查经营年限
        if "经营满" in "".join(policy.eligibility):
            for req in policy.eligibility:
                if "年" in req:
                    years = int(re.search(r'(\d+)', req).group(1)) if re.search(r'(\d+)', req) else 0
                    if profile.business_age >= years:
                        qualified_conditions.append(f"✓ 经营年限满足要求")
                    else:
                        missing_items.append(f"✗ 需经营满{years}年")
                    break
        
        return {
            "qualified": len(missing_items) == 0,
            "conditions": qualified_conditions,
            "missing_items": missing_items
        }
    
    def _estimate_subsidy(self, policy: Policy, profile: UserProfile) -> Dict[str, Any]:
        """估算补贴金额"""
        info = policy.subsidy_info
        
        if info.get("type") == "税收减免":
            # 税收减免按比例估算
            tax_savings = profile.annual_revenue * 0.1 * 0.25  # 简化估算
            return {
                "min": 0,
                "max": min(tax_savings, 100),  # 上限100万
                "unit": "万元",
                "calculation_basis": f"基于年营收{profile.annual_revenue/10000:.1f}万元估算"
            }
        else:
            return {
                "min": info.get("min", 0),
                "max": info.get("max", 0),
                "unit": info.get("unit", "万元"),
                "calculation_basis": "官方标准"
            }
    
    def _generate_risk_alerts(self, policy: Policy, profile: UserProfile) -> List[str]:
        """生成风险提示"""
        alerts = []
        
        # 截止日期风险
        deadline = datetime.strptime(policy.deadline, "%Y-%m-%d")
        days_left = (deadline - datetime.now()).days
        if days_left < 7:
            alerts.append(f"⚠️ 紧急：距截止仅剩{days_left}天，请尽快申报！")
        elif days_left < 30:
            alerts.append(f"⏰ 提醒：距截止还有{days_left}天")
        
        # 材料准备风险
        if len(policy.materials) > 5:
            alerts.append("📋 注意：所需材料较多，建议提前准备")
        
        # 时间风险
        total_days = self._calculate_total_time_days(policy)
        if total_days > days_left:
            alerts.append("⚠️ 警告：申报周期可能超过剩余时间")
        
        return alerts
    
    def _calculate_total_time(self, policy: Policy) -> str:
        """计算总申报时间"""
        total_days = self._calculate_total_time_days(policy)
        if total_days < 30:
            return f"约{total_days}个工作日"
        else:
            return f"约{total_days//30}个月"
    
    def _calculate_total_time_days(self, policy: Policy) -> int:
        """计算总申报天数"""
        return sum([step.get("duration_days", 5) for step in policy.application_steps])
    
    def _assess_urgency(self, deadline: str) -> str:
        """评估紧急程度"""
        try:
            deadline_dt = datetime.strptime(deadline, "%Y-%m-%d")
            days_left = (deadline_dt - datetime.now()).days
            if days_left < 7:
                return "high"
            elif days_left < 30:
                return "medium"
            else:
                return "low"
        except:
            return "unknown"


class PolicyMatcher:
    """政策匹配器"""
    
    def __init__(self, search_engine: PolicySearchEngine):
        self.search_engine = search_engine
    
    def match_policy(self, user_profile: Dict, focus_areas: List[str] = None, limit: int = 10) -> Dict[str, Any]:
        """
        智能匹配政策
        
        Args:
            user_profile: 用户画像
            focus_areas: 关注的政策领域
            limit: 返回数量限制
        
        Returns:
            个性化政策推荐
        """
        profile = UserProfile(
            region=user_profile.get("region", ""),
            industry=user_profile.get("industry", ""),
            company_type=user_profile.get("company_type", ""),
            employee_count=user_profile.get("employee_count", 0),
            annual_revenue=user_profile.get("annual_revenue", 0),
            qualifications=user_profile.get("qualifications", []),
            business_age=user_profile.get("business_age", 0),
            is_high_tech=user_profile.get("is_high_tech", False),
            is_small_micro=user_profile.get("is_small_micro", False),
            focus_areas=focus_areas or []
        )
        
        matched = []
        
        for policy in self.search_engine.policies:
            # 计算综合得分
            match_score = self._calculate_match_score(policy, profile)
            success_prob = self._estimate_success_probability(policy, profile)
            estimated_subsidy = self._get_max_subsidy(policy, profile)
            urgency = self._assess_policy_urgency(policy)
            
            # 匹配原因
            reasons = self._generate_match_reasons(policy, profile)
            
            matched.append({
                "policy_id": policy.policy_id,
                "title": policy.title,
                "match_score": match_score,
                "success_probability": success_prob,
                "estimated_subsidy": estimated_subsidy,
                "urgency": urgency,
                "reasons": reasons,
                "deadline": policy.deadline,
                "policy_type": policy.policy_type
            })
        
        # 综合排序
        matched.sort(key=lambda x: (
            x["match_score"] * 0.4 + 
            x["success_probability"] * 0.3 + 
            x["estimated_subsidy"] / 100 * 0.3
        ), reverse=True)
        
        # 添加优先级标签
        for i, policy in enumerate(matched[:limit]):
            if i == 0:
                policy["priority"] = "⭐ 强烈推荐"
            elif policy["urgency"] == "high":
                policy["priority"] = "🔥 即将截止"
            elif policy["success_probability"] > 80:
                policy["priority"] = "✅ 高匹配度"
            else:
                policy["priority"] = "📌 推荐关注"
        
        return {
            "matched_policies": matched[:limit],
            "total_matched": len(matched),
            "recommendations": self._generate_recommendations(matched[:limit], profile)
        }
    
    def _calculate_match_score(self, policy: Policy, profile: UserProfile) -> float:
        """计算匹配度得分 (0-100)"""
        score = 0
        
        # 地域匹配 (20分)
        if profile.region in policy.region:
            score += 20
        elif policy.region == "national":
            score += 15
        
        # 行业匹配 (25分)
        if profile.industry in policy.industry:
            score += 25
        elif policy.industry == "general":
            score += 15
        
        # 资质匹配 (30分)
        qualification_match = len([q for q in profile.qualifications if q in str(policy.eligibility)])
        score += min(qualification_match * 15, 30)
        
        # 企业规模匹配 (15分)
        if policy.policy_type == "企业培育":
            if profile.is_high_tech or profile.employee_count >= 10:
                score += 15
        
        # 关注领域匹配 (10分)
        if profile.focus_areas:
            if any(area in policy.policy_type for area in profile.focus_areas):
                score += 10
        
        return min(score, 100)
    
    def _estimate_success_probability(self, policy: Policy, profile: UserProfile) -> float:
        """评估申报成功率"""
        prob = 70.0  # 基础成功率
        
        # 地域完全匹配
        if profile.region == policy.region:
            prob += 10
        
        # 行业匹配
        if profile.industry == policy.industry:
            prob += 10
        
        # 小微企业专项
        if policy.policy_type == "税收优惠" and profile.is_small_micro:
            prob += 10
        
        # 高新企业专项
        if "科技" in policy.industry and profile.is_high_tech:
            prob += 5
        
        return min(prob, 95)
    
    def _get_max_subsidy(self, policy: Policy, profile: UserProfile) -> float:
        """获取最大补贴金额"""
        return policy.subsidy_info.get("max", 0)
    
    def _assess_policy_urgency(self, policy: Policy) -> str:
        """评估政策紧急程度"""
        try:
            deadline_dt = datetime.strptime(policy.deadline, "%Y-%m-%d")
            days_left = (deadline_dt - datetime.now()).days
            if days_left < 7:
                return "high"
            elif days_left < 30:
                return "medium"
            else:
                return "low"
        except:
            return "low"
    
    def _generate_match_reasons(self, policy: Policy, profile: UserProfile) -> List[str]:
        """生成匹配原因"""
        reasons = []
        
        if profile.region in policy.region:
            reasons.append(f"地域适用：{policy.region}")
        elif policy.region == "national":
            reasons.append("全国通用政策")
        
        if profile.industry == policy.industry:
            reasons.append(f"行业匹配：{policy.industry}行业")
        
        if policy.subsidy_info.get("max", 0) > 50:
            reasons.append(f"高额补贴：最高{policy.subsidy_info['max']}万元")
        
        try:
            days_left = (datetime.strptime(policy.deadline, "%Y-%m-%d") - datetime.now()).days
            if days_left > 0:
                reasons.append(f"距截止{days_left}天")
        except:
            pass
        
        return reasons
    
    def _generate_recommendations(self, matched: List[Dict], profile: UserProfile) -> str:
        """生成整体建议"""
        if not matched:
            return "暂无完全匹配的政策，建议关注最新政策发布"
        
        recommendations = []
        
        # 高匹配度政策建议
        high_match = [p for p in matched if p["match_score"] >= 70]
        if high_match:
            recommendations.append(f"您有{len(high_match)}个高匹配度政策，建议优先申报")
        
        # 即将截止提醒
        urgent = [p for p in matched if p["urgency"] == "high"]
        if urgent:
            titles = "、".join([p["title"][:10] for p in urgent])
            recommendations.append(f"⚠️ 即将截止：{titles}")
        
        # 补贴最高的政策
        if matched:
            max_subsidy = max(matched, key=lambda x: x["estimated_subsidy"])
            if max_subsidy["estimated_subsidy"] > 0:
                recommendations.append(f"💰 补贴最高：{max_subsidy['title']}（最高{max_subsidy['estimated_subsidy']}万元）")
        
        return "；".join(recommendations) if recommendations else "建议持续关注政策更新"


class PolicyReminder:
    """政策提醒服务"""
    
    def __init__(self, search_engine: PolicySearchEngine):
        self.search_engine = search_engine
    
    def get_reminders(
        self,
        subscribed_policies: List[str] = None,
        reminder_days: List[int] = None
    ) -> Dict[str, Any]:
        """
        获取政策提醒
        
        Args:
            subscribed_policies: 订阅的政策ID列表
            reminder_days: 提前提醒天数列表
        
        Returns:
            提醒列表
        """
        reminder_days = reminder_days or [7, 14, 30]
        today = datetime.now()
        
        reminders = []
        new_policies = []
        warning_policies = []
        
        for policy in self.search_engine.policies:
            try:
                deadline_dt = datetime.strptime(policy.deadline, "%Y-%m-%d")
                days_remaining = (deadline_dt - today).days
                
                # 检查是否需要提醒
                if days_remaining > 0:
                    for day in reminder_days:
                        if day - 3 <= days_remaining <= day + 3:
                            urgency_level = "high" if days_remaining <= 7 else "medium" if days_remaining <= 14 else "low"
                            reminders.append({
                                "policy_id": policy.policy_id,
                                "title": policy.title,
                                "deadline": policy.deadline,
                                "days_remaining": days_remaining,
                                "urgency_level": urgency_level,
                                "action_required": "立即申报" if days_remaining <= 7 else "准备材料" if days_remaining <= 14 else "提前规划"
                            })
                            break
                
                # 即将截止警告
                if 0 < days_remaining <= 7:
                    warning_policies.append({
                        "policy_id": policy.policy_id,
                        "title": policy.title,
                        "days_remaining": days_remaining
                    })
                
                # 新政（发布30天内）
                publish_dt = datetime.strptime(policy.publish_date, "%Y-%m-%d")
                if (today - publish_dt).days <= 30:
                    new_policies.append({
                        "policy_id": policy.policy_id,
                        "title": policy.title,
                        "publish_date": policy.publish_date
                    })
                    
            except ValueError:
                continue
        
        # 排序
        reminders.sort(key=lambda x: x["days_remaining"])
        
        return {
            "reminders": reminders,
            "new_policies": new_policies,
            "warning_policies": warning_policies
        }


# 导出主要类
__all__ = [
    "Policy",
    "UserProfile", 
    "PolicySearchEngine",
    "PolicyAnalyzer",
    "PolicyMatcher",
    "PolicyReminder"
]


if __name__ == "__main__":
    # 演示代码
    print("=== 政策拆解分析器演示 ===\n")
    
    # 初始化
    search_engine = PolicySearchEngine()
    analyzer = PolicyAnalyzer(search_engine)
    matcher = PolicyMatcher(search_engine)
    
    # 1. 搜索政策
    print("【政策搜索】搜索深圳创业政策：")
    results = search_engine.search_policy(region="深圳", policy_type="创业扶持")
    for p in results["policies"][:3]:
        print(f"  - {p['title']} (匹配度:{p['match_score']})")
    
    print("\n【政策搜索】搜索科技型中小企业政策：")
    results = search_engine.search_policy(keywords="科技型中小企业")
    for p in results["policies"][:3]:
        print(f"  - {p['title']}")
    
    # 2. 深度解析
    print("\n【政策解析】分析专精特新企业培育计划：")
    user_profile = {
        "region": "深圳",
        "industry": "制造业",
        "company_type": "民营企业",
        "employee_count": 150,
        "annual_revenue": 30000000,
        "business_age": 5,
        "is_high_tech": True,
        "is_small_micro": False
    }
    analysis = analyzer.analyze_policy("POL20240005", user_profile)
    print(f"  匹配状态: {'✓ 符合条件' if analysis['eligibility']['qualified'] else '✗ 部分条件不符'}")
    print(f"  符合条件: {', '.join(analysis['eligibility']['conditions'][:3])}")
    print(f"  补贴估算: 最高{analysis['subsidy_estimate']['max']}万元")
    print(f"  申报周期: {analysis['application_process']['estimated_time']}")
    print(f"  风险提示: {' '.join(analysis['risk_alerts'])}")
    
    # 3. 智能匹配
    print("\n【智能匹配】个性化政策推荐：")
    match_result = matcher.match_policy(
        user_profile=user_profile,
        focus_areas=["创业扶持", "企业培育", "税收优惠"],
        limit=5
    )
    print(f"  共匹配 {match_result['total_matched']} 个政策")
    for p in match_result["matched_policies"][:3]:
        print(f"  [{p['priority']}] {p['title']}")
        print(f"    匹配度:{p['match_score']} | 成功率:{p['success_probability']}% | 最高补贴:{p['estimated_subsidy']}万元")
        print(f"    原因:{', '.join(p['reasons'][:2])}")
    print(f"\n  整体建议: {match_result['recommendations']}")
