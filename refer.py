class Marketing:
      all_rs = {}
      all_points = {}
      def __init__(self, ism, familiya, user):
            self.ism = ism
            self.familiya = familiya
            self.user = user
            self.r1 = ''
            self.rs = []
            Marketing.all_points[self.user] = 0
            
      def referral(self):
            import random
            r = ''
            for _ in range(6):
                  r += str(random.randint(0, 9))
                  if r not in self.rs:
                        self.r1 = r
                        
                        self.rs.append(self.r1)
            Marketing.all_rs[self.r1] = self.user
            return self.r1
          
      def qowil(self, ref):
            
            if ref in list(Marketing.all_rs.keys()):
                  Marketing.all_points[Marketing.all_rs.get(ref)] += 1
                  
            else:
                  pass
                  
                  
          







