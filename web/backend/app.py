from flask import send_from_directory

from api.services.extract_api import extract_api  # 导入提取API蓝图
from api.services.assessment_api import assessment_api  # 导入评估API蓝图
from api.services.transcribe_api import transcribe_api  # 导入转录API蓝图
from api import auth, menu, test, user, userAnalyse
from utils.database import init_dataset
from utils.extensions import app

init_dataset(app)


@app.route("/")
def index():
    return send_from_directory("dist", "index.html")



app.register_blueprint(transcribe_api)  # 注册转录API蓝图
app.register_blueprint(extract_api)  # 注册提取API蓝图
app.register_blueprint(assessment_api)  # 注册评估API蓝图
app.register_blueprint(auth.bp)
app.register_blueprint(menu.bp)
app.register_blueprint(test.bp)
app.register_blueprint(user.bp)
app.register_blueprint(userAnalyse.bp)
if __name__ == "__main__":
    app.run(debug=True, port=8000)  # 开启调试模式（包含热重载）
