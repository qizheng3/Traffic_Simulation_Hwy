    def mainloop(self):
        self.root.mainloop()
        


if __name__ == '__main__':
    UI = UI()
    for highway in range(10):
        UI.display(highway)
    UI.mainloop()
