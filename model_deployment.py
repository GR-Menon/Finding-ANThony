from fastai.vision.all import *
import gradio as gr


class Interface:
    def __init__(self, model, categories, examples):
        self.model = model
        self.examples = examples
        self.categories = categories
    
    def classify(self,img):
        pred, idx, probs = self.model.predict(img)
        return dict(zip(self.categories, map(float, probs)))
    
    def create_interface(self):
        image = gr.inputs.Image(shape=(256,256))
        label = gr.outputs.Label()
        
        interface = gr.Interface(fn=self.classify, inputs=image, outputs=label, examples=self.examples)
        interface.launch(inline=False,share=True)


# categories = ('Ant','Termite')

# def classify(model, img):
#     preds, idx, probs = model.predict(img)
#     return dict(zip(categories,map(float,probs) ))

# def create_Gradio_interface(model_file='model.pkl', pred_function=classify, img_examples=None):
#     model = pickle.load(open(model_file,'rb'))
    
#     image = gr.inputs.Image(shape=(256,256))
#     label = gr.outputs.Label()
    
#     interface = gr.Interface(fn=pred_function, inputs=image, outputs=label, examples=img_examples)
#     interface.launch(inline=False,share=True)



    
    
    
        
