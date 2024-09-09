
class Risk:
    def __init__(self, name, risk_level):
        self.name = name
        self.risk_level = risk_level

    def add_numbers(a, b):
        return a + b

    def subtract_numbers(a, b):
        return a - b

    def calculate_risk_level(report_count, report_source, custom_risk_level):
        """_summary_

        Args:
            report_count (_type_): 通報次數
            report_source (_type_): 通報來源
            custom_risk_level (_type_): 業者自訂風險等級

# 函数首先定义了各参数的权重,然后根据输入计算每个参数的得分。最后,将这些得分相加得到总分,并根据总分确定最终的风险等级。
# 风险等级的判断标准如下:
# 总分 >= 1.2: 高风险
# 0.7 <= 总分 < 1.2: 中高风险
# 总分 < 0.7: 中风险
#
        Returns:
            _type_: _description_
        """
        # 定義通報次數的權重區間
        if report_count > 5:
            report_count_weight = 0.5
        elif 3 <= report_count <= 5:
            report_count_weight = 0.3
        else:
            report_count_weight = 0.2

        # 定義通報來源的權重
        report_source_weights = {
            "檢警調通知": 0.9,
            "金融機構通知": 0.5,
            "業者KYC": 0.2
        }

        # 定義業者自訂風險等級的權重
        custom_risk_weights = {
            "極高": 0.5,
            "高": 0.3,
            "中": 0.2
        }

        # 獲取通報來源和業者自訂風險等級的權重
        report_source_weight = report_source_weights.get(report_source, 0)
        custom_risk_weight = custom_risk_weights.get(custom_risk_level, 0)

        # 計算風險分數
        total_score = report_count_weight + report_source_weight + custom_risk_weight
        # print(total_score, report_count_weight,
        #       report_source_weight, custom_risk_weight)

        # 判斷風險等級
        if total_score < 0.7:
            return "中度風險"
        elif total_score < 1.2:
            return "中高度風險"
        else:
            return "高度風險"
