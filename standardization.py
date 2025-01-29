from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def concat_and_standardization(data):
    df_list = []
    for d in data:
        df = pd.DataFrame(d)
        df_list.append(df)
    df = pd.concat(df_list, ignore_index=True)

    X = df[['F1', 'F2']]
    y = df['ラベル']

    scaler = StandardScaler()
    X_normalized = scaler.fit_transform(X)

    print("正規化後のデータ:")
    print(X_normalized)
    
    X_train, X_test, y_train, y_test = train_test_split(X_normalized, y, test_size=0.2, random_state=42)

    model = LogisticRegression(random_state=42, max_iter=1000)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"モデルの精度: {accuracy * 100:.2f}%")

    new_data = [[350, 1200], [400, 1100]]
    new_data_normalized = scaler.transform(new_data)
    predicted_labels = model.predict(new_data_normalized)
    print(f"予測されたラベル: {predicted_labels}")
    