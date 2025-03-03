package logger

import (
	"go.uber.org/zap"
	"go.uber.org/zap/zapcore"
)

// private so we only make available the helper functions
// that way we don't couple the code to a log framework(zap)
var log *zap.Logger

func init() {
	// init functions run after a package is imported
	// in this case this module is imported in the main.go
	var err error

    config := zap.NewProductionConfig()

    encoderConfig := zap.NewProductionEncoderConfig()
    encoderConfig.TimeKey = "timestamp"
    encoderConfig.EncodeTime = zapcore.ISO8601TimeEncoder
    // this is for Error log to not see the stacktrace
    encoderConfig.StacktraceKey = ""

    config.EncoderConfig = encoderConfig

    log, err = config.Build(zap.AddCallerSkip(1))

    // AddCallerSkip allows to wrap the log and prevent the call
    // to be recorded as being by the helper funcion
    // the 1 is the level of wraps.
	// log, err = zap.NewProduction(zap.AddCallerSkip(1))

	if err != nil {
		panic(err)
	}
}

func Info(message string, fields ...zap.Field) {
    log.Info(message, fields...)
}

func Debug(message string, fields ...zap.Field) {
    log.Debug(message, fields...)
}

func Warn(message string, fields ...zap.Field) {
    log.Warn(message, fields...)
}

func Error(message string, fields ...zap.Field) {
    log.Error(message, fields...)
}
