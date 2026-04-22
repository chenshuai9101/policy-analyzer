#!/usr/bin/env python3
"""
Policy-Analyzer 测试用例
验证政策检索、解析、匹配功能
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from scripts.policy_engine import (
    PolicySearchEngine,
    PolicyAnalyzer,
    PolicyMatcher,
    PolicyReminder
)

def test_policy_search():
    """测试政策检索"""
    print("=== 测试: 政策检索 ===")
    
    engine = PolicySearchEngine()
    
    results = engine.search_policy(
        keywords="科技型中小企业",
        region="深圳",
        industry="科技",
        policy_type="创业扶持"
    )
    
    assert "policies" in results
    assert "total" in results
    print(f"✅ 政策检索成功，找到 {results['total']} 条政策")
    
    return True

def test_policy_analyze():
    """测试政策解析"""
    print("\n=== 测试: 政策解析 ===")
    
    engine = PolicySearchEngine()
    analyzer = PolicyAnalyzer(engine)
    
    analysis = analyzer.analyze_policy(
        policy_id="POL20240001",
        user_profile={
            "region": "深圳",
            "industry": "互联网",
            "employee_count": 15,
            "is_small_micro": True
        }
    )
    
    print(f"✅ 政策解析成功")
    
    return True

def test_policy_match():
    """测试政策匹配"""
    print("\n=== 测试: 政策匹配 ===")
    
    engine = PolicySearchEngine()
    matcher = PolicyMatcher(engine)
    
    recommendations = matcher.match_policy(
        user_profile={
            "region": "深圳",
            "industry": "科技",
            "employee_count": 50,
            "is_small_micro": True
        },
        focus_areas=["补贴", "税收优惠"],
        limit=5
    )
    
    assert "matched_policies" in recommendations
    print(f"✅ 政策匹配成功")
    
    return True

def test_reminder():
    """测试时效提醒"""
    print("\n=== 测试: 时效提醒 ===")
    
    engine = PolicySearchEngine()
    reminder = PolicyReminder(engine)
    
    alerts = reminder.get_reminders(reminder_days=[7, 14, 30])
    
    assert "reminders" in alerts
    print(f"✅ 时效提醒功能正常")
    
    return True

def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("Policy-Analyzer 测试套件")
    print("=" * 50)
    
    tests = [
        test_policy_search,
        test_policy_analyze,
        test_policy_match,
        test_reminder,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"❌ 测试失败: {e}")
            failed += 1
    
    print("\n" + "=" * 50)
    print(f"测试结果: {passed} 通过, {failed} 失败")
    print("=" * 50)
    
    return failed == 0

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
