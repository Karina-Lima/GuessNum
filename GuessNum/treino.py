import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

mnist = tf.keras.datasets.mnist
(atreinar, btreinar), (ateste, bteste) = mnist.load_data()

escolha = input("Deseja treinar a rede? (s/n): ")

if escolha == "s":
    
    atreinar = atreinar / 255.0
    ateste = ateste / 255.0
    
    atreinar = atreinar.reshape(atreinar.shape[0], 28, 28, 1)
    ateste = ateste.reshape(ateste.shape[0], 28, 28, 1)
   
    datagen = ImageDataGenerator(
        rotation_range=10,
        width_shift_range=0.1,
        height_shift_range=0.1,
        zoom_range=0.1
    )
    datagen.fit(atreinar)

    # Definir o modelo
    modelo = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28, 1)),  # Incluindo canal
        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(128, activation="relu"),
        tf.keras.layers.Dropout(0.3),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    modelo.compile(
        optimizer="adam",  
        loss="sparse_categorical_crossentropy",
        metrics=["accuracy"]
    )

   
    modelo.fit(datagen.flow(atreinar, btreinar, batch_size=64), 
               validation_data=(ateste, bteste),
               epochs=50)  

    modelo.save("cachola.keras")
    print("Modelo treinado e salvo com sucesso!")
else:
    print("Treinamento não realizado!")
