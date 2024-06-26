import dlib
import cv2

# Dlibの顔ランドマーク検出器を初期化
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# 入力画像の読み込み
image = cv2.imread("Your Path")

# グレースケールに変換
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 顔の検出
faces = detector(gray)

for face in faces:
    # 顔領域のランドマークを検出
    landmarks = predictor(gray, face)
    
    # 口のランドマークのインデックス
    mouth_indices = list(range(48, 68))  # 口のランドマークは48〜67の範囲にあります
    
    # 口のランドマークを抽出
    mouth_points = [(landmarks.part(i).x, landmarks.part(i).y) for i in mouth_indices]
    
    # 口の輪郭を描画
    for i in range(len(mouth_points) - 1):
        cv2.line(image, mouth_points[i], mouth_points[i + 1], (0, 255, 0), 2)

# 結果を表示
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
a
