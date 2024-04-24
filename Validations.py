class Validations:
    def __init__(self):
        self.colors_order = [5,3,1,6,4,2]
        self.validations_dict = {0:"",1:"",2:"",3:"",4:"",5:"",6:""}
        self.count_pieces = {}
        
    def validate_centers_orientation(self, faces):#5
        for index in range(len(self.colors_order)):
            if self.colors_order[index] != faces[index][1][1]:
                self.validations_dict[5] = "El centro:"+str(self.colors_order[index])+" está mal orientado"
                return False
        return True
    
    def validate_centers_different(self, faces):#5
        count = {}
        for face in faces:
            count[face[1][1]] = count.get(face[1][1], 0) + 1
            if count[face[1][1]] > 1:
                self.validations_dict[4] = "Hay 2 o más centros del mismo color"
                return False
        return True 
    
    def validate_count_faces(self,faces):#1
        if len(faces) != 6:
            self.validations_dict[0] = "La cantidad de caras ingresada es: "+str(len(faces))+", la cantidad correcta debe ser 6."
            return False
        return True
    
    def validate_size_rows(self,face):#2
        if len(face) != 3:
            self.validations_dict[1] = "La cantidad de filas en una de las caras es: "+str(len(face))+ ", la cantidad correcta debe ser 3."
            return False
        return True
    
    def validate_size_columns(self,face):#3
        for row in face:
            if len(row) != 3:
                self.validations_dict[2] = "La cantidad de columnas en una de las filas es: "+str(len(row))+", la cantidad correcta debe ser 3."
                return False
        return True
    
    def validate_count_colors_in_face(self,face):#4
        for row in face:
            for column in row:
                if column not in self.count_pieces:
                    self.count_pieces[column] = self.count_pieces.get(column, 0)
                self.count_pieces[column] += 1
                if self.count_pieces[column] > 9:
                    self.validations_dict[3] = "La cantidad de piezas de un mismo color ingresadas es de: "+str(self.count_pieces[column])+", la cantidad correcta debe ser 9 por color."
                    return False
        return True
    
    def validate_count_colors(self,faces):
        colors = set()
        for face in faces:
            for row in face:
                for column in row:
                    colors.add(column)
        if len(colors) != 6:
            self.validations_dict[6] = "Hay "+str(len(colors))+" colores diferentes en el cubo, tienen ser 6."
            return False
        return True
    
    def get_result_validations(self, faces):
        if not self.validate_count_faces(faces):
            return self.validations_dict[0]
        if not self.validate_count_colors(faces):
            return self.validations_dict[6]
        for face in faces:
            if not self.validate_size_rows(face):
                return self.validations_dict[1]
            if not self.validate_size_columns(face):
                return self.validations_dict[2]
            if not self.validate_count_colors_in_face(face):
                return self.validations_dict[3]
        if not self.validate_centers_different(faces):
            return self.validations_dict[4]
        if not self.validate_centers_orientation(faces):
            return self.validations_dict[5]
        return "Correcto"
        
                
        