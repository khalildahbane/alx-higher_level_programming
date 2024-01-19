#!/usr/bin/node

class Rectangle {
    constructor(w, h) {
        if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
        }
    if (w === undefined || h === undefined) {
        return Rectangle = {};
        }
    }
}

module.exports = Rectangle;