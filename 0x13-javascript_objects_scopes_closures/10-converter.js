#
rts.converter = function (base) {
  return function (arg) {
    return parseInt(arg, 10).toString(base);
  };
};
