import joblib





def preparing(data):
    df = pd.read_csv('/data/dt.csv')

    return df

print(a)


'''

#preparation des donnés

le= LabelEncoder()
y = le.fit_transform(y)
print(len(y))




X_train, X_test, y_train, y_test = train_test_split(
    x,y,
    test_size =0.2,
    random_state= 42,)

preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_cols),
        ('cat', OneHotEncoder(drop='first'), cat_cols)
    ]
)
models ={
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(random_state=42)

}

param_grids = {
    "LogisticRegression": {
        'model__C': [0.01, 0.1, 1, 10]
    },
    "RandomForest": {
        'model__n_estimators': [200, 500],
        'model__max_depth': [4, 5, 6, 7, 8],
        'model__criterion':['gini', 'entropy']
    }
}
model = LogisticRegression()

pipeline = Pipeline([
        ('preprocessor', preprocessor),
        ('model', model)
    ])

pipeline.fit(X_train,y_train)'''